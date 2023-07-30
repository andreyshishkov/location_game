from flask import Flask, render_template
from location_game.forms import MessageForm
from location_game.config import Config
from location_game.game import Game
from location_game.exceptions import ImpossibleStepException


app = Flask(__name__)
app.config.from_object(Config)


@app.route('/', methods=['GET'])
def start_page():
    game = Game()
    game.reinitialize()
    return render_template(
        'start_page.html',
    )


@app.route('/game/', methods=['GET', 'POST'])
def game_page():
    game = Game()
    is_start_of_game = True
    form = MessageForm()
    if form.validate_on_submit():
        is_start_of_game = False

        way = form.way.data
        num_steps = form.number_steps.data
        try:
            game.make_step(way, num_steps)
        except ImpossibleStepException:
            return render_template(
                'game.html',
                form=form,
                game=game,
                is_start_of_game=is_start_of_game,
                error=True
            )

    return render_template(
        'game.html',
        form=form,
        game=game,
        is_state_of_page=is_start_of_game,
        error=False
    )


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
