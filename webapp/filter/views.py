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
        process = process_general_CSV_from_filter(filter=form.filter.data,
                                                  jira_api_key=form.token.data)
        if process['bool']:
            flash(process['text'])
            return send_file(f'issues_from_filter_{form.filter.data}.csv')
        else:
            flash(process['error'])
    return redirect(url_for('search.index'))
