from flask import (Blueprint, render_template, flash,
                   redirect, url_for, send_file)


from webapp.status_jira import status_jira
from webapp.filter.forms import SearchForm
from webapp.issues_filter import process_general_CSV_from_filter

# Родительский URL
blueprint = Blueprint('search', __name__)


@blueprint.route('/')
def index():
    title = "Микросервис отчетов Jira"
    status = status_jira()
    # Создание экземпляра класса
    search_form = SearchForm()
    return render_template('base.html', page_title=title,
                           status=status, form=search_form)


@blueprint.route('/process-search', methods=['POST'])
def process_search():
    form = SearchForm()

    if form.validate_on_submit():
        process_general_CSV_from_filter(filter=form.filter.data,
                                        jira_api_key=form.token.data)
        flash('Был сформирован файл CSV')
        return send_file(f'issues_from_filter_{form.filter.data}.csv')
        # return redirect(url_for('news.index'))
    else:
        flash('Неправильный токен или ID фильтра')
    return redirect(url_for('search.index'))
