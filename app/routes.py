from flask import Blueprint, render_template, request, redirect, url_for, flash
from .models import db, cliente, item, atendimento, categoria, fornecedor
from datetime import datetime

main_bp = Blueprint('main', __name__)

# --- ROTAS DA LOJA (Frontend) ---

@main_bp.route('/loja')
def loja_index():
    # Busca itens (produtos/serviços) no banco para mostrar na loja
    itens_destaque = item.query.limit(8).all() # Pega os 8 primeiros, por exemplo
    return render_template('index.html', itens_destaque=itens_destaque)

@main_bp.route('/login')
def login():
    return render_template('login.html')

@main_bp.route('/carrinho')
def carrinho():
    return render_template('carrinho.html')

@main_bp.route('/produtos')
def produtos():
    # Aqui você poderia adicionar lógica pra filtrar por categoria (request.args.get('categoria'))
    categoria_slug = request.args.get('categoria')
    # Por enquanto, apenas renderiza a página estática
    return render_template('produtos.html', categoria_selecionada=categoria_slug)

# --- ROTA DO PAINEL ADMIN (Backend) ---

@main_bp.route('/') # Rota principal (/) é o dashboard
def index():
    todos_clientes = cliente.query.all()
    todos_itens = item.query.all()
    todos_atendimentos = atendimento.query.order_by(atendimento.data_atendimento.desc()).all()
    categorias_disponiveis = categoria.query.all()
    fornecedores_disponiveis = fornecedor.query.all()

    total_clientes = cliente.query.count()
    total_itens = item.query.count()
    total_atendimentos = atendimento.query.count()

    return render_template(
        'dashboard.html',
        clientes=todos_clientes,
        itens=todos_itens,
        atendimentos=todos_atendimentos,
        categorias=categorias_disponiveis,
        fornecedores=fornecedores_disponiveis,
        total_clientes=total_clientes,
        total_itens=total_itens,
        total_atendimentos=total_atendimentos
    )

# --- ROTAS DE CRUD (Clientes, Itens, Atendimentos) ---
# (As rotas add_cliente, delete_cliente, add_item, delete_item, add_atendimento, delete_atendimento continuam iguais às da resposta anterior)

@main_bp.route('/clientes/add', methods=['POST'])
def add_cliente():
    try:
        novo_cliente = cliente(
            nome=request.form.get('nome_cliente'),
            email=request.form.get('email_cliente'),
            telefone=request.form.get('telefone_cliente'),
            endereco=request.form.get('endereco_cliente'),
            cpf=request.form.get('cpf_cliente')
        )
        db.session.add(novo_cliente)
        db.session.commit()
        flash('Cliente cadastrado com sucesso!', 'success')
    except Exception as e:
        db.session.rollback()
        flash(f'Erro ao cadastrar cliente: {str(e)}', 'error')
    return redirect(url_for('main.index'))

@main_bp.route('/clientes/delete/<int:id>')
def delete_cliente(id):
    cli = cliente.query.get_or_404(id)
    try:
        db.session.delete(cli)
        db.session.commit()
        flash('Cliente removido.', 'success')
    except Exception as e:
        db.session.rollback()
        flash(f'Erro ao remover cliente: {str(e)}', 'error')
    return redirect(url_for('main.index'))

@main_bp.route('/item/add', methods=['POST'])
def add_item():
    try:
        novo_item = item(
            nome=request.form.get('nome_item'),
            descricao=request.form.get('descricao_item'),
            preco=float(request.form.get('valor_item')),
            tipo=request.form.get('tipo_item'),
            estoque=int(request.form.get('estoque_item', 0)),
            categoria_id=int(request.form.get('categoria_id')),
            fornecedor_id=int(request.form.get('fornecedor_id'))
        )
        db.session.add(novo_item)
        db.session.commit()
        flash(f'Item ({novo_item.tipo}) cadastrado com sucesso!', 'success')
    except Exception as e:
        db.session.rollback()
        flash(f'Erro ao cadastrar item: {str(e)}', 'error')
    return redirect(url_for('main.index'))

@main_bp.route('/item/delete/<int:id>')
def delete_item(id):
    it = item.query.get_or_404(id)
    try:
        db.session.delete(it)
        db.session.commit()
        flash('Item removido.', 'success')
    except Exception as e:
        db.session.rollback()
        flash(f'Erro ao remover item: {str(e)}', 'error')
    return redirect(url_for('main.index'))

@main_bp.route('/atendimentos/add', methods=['POST'])
def add_atendimento():
    try:
        novo_atendimento = atendimento(
            cliente_id=int(request.form.get('cliente_id')),
            data_atendimento=datetime.utcnow()
        )
        db.session.add(novo_atendimento)
        db.session.commit()
        flash('Atendimento registrado com sucesso!', 'success')
    except Exception as e:
        db.session.rollback()
        flash(f'Erro ao registrar atendimento: {str(e)}', 'error')
    return redirect(url_for('main.index'))

@main_bp.route('/atendimentos/delete/<int:id>')
def delete_atendimento(id):
    at = atendimento.query.get_or_404(id)
    try:
        db.session.delete(at)
        db.session.commit()
        flash('Atendimento removido.', 'success')
    except Exception as e:
        db.session.rollback()
        flash(f'Erro ao remover atendimento: {str(e)}', 'error')
    return redirect(url_for('main.index'))