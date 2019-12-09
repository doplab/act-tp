(() => {
    const SIDES = 600;
    const CELLS = 30;
    const CELL_WH = SIDES / CELLS;

    class Square {
        constructor(x, y, alive = true) {
            this.x = x;
            this.y = y;
            this.alive = alive;
        }

        render(ctx) {
            if (this.alive) {
                ctx.rect(this.x, this.y, CELL_WH, CELL_WH);
            }
        }
    }

    const consoleDiv = document.querySelector('#console');
    const errorsDiv = document.querySelector('#errors');

    const pythonPromise = squares =>
        new Promise((resolve, reject) => {
            const callbacks = {
                iopub: {
                    output: data => {
                        try {
                            let { text } = data.content;
                            const errorsRe = new RegExp("(?<=JUPYTER_EXCEPTION)(.*)(?=END_JUPYTER_EXCEPTION)");
                            const exceptions = text
                                .trim()
                                .split('\n')
                                .join('<br/>')
                                .match(errorsRe);
                            if (exceptions) {
                                errorsDiv.innerHTML += exceptions[0];
                                errorsDiv.innerHTML += '<br/>';
                                text = text
                                    .trim()
                                    .split('\n')
                                    .join('<br/>')
                                    .replace(/(JUPYTER_EXCEPTION)(.*)(END_JUPYTER_EXCEPTION)/, '');
                            }
                            const split = text.trim().split('\n');
                            const json = split.pop();
                            text = split.join('<br/>');
                            if (text.length) {
                                consoleDiv.innerHTML += text;
                                consoleDiv.innerHTML += '<br/>';
                            }
                            resolve(json.split("'").join('"'));
                        } catch (err) {
                            reject(err);
                        }
                    }
                }
            };
            IPython.notebook.kernel.execute(`Binder.instance.update_data(${squares})`, callbacks);
        });

    class Game {
        constructor() {
            this.squares = [];
            this.up;
            const canvas = document.querySelector('#game');
            this.ctx = canvas.getContext('2d');

            this.stopped = true;
            this.fails = 0;

            if (!Game.intervals) Game.intervals = [];
            else {
                Game.intervals.forEach(interval => window.clearTimeout(interval));
                Game.intervals = [];
            }

            this.render = this.render.bind(this);
            this.start = this.start.bind(this);
            this.updateData = this.updateData.bind(this);
            this.updateKernel = this.updateKernel.bind(this);
            this.stop = this.stop.bind(this);
        }

        render() {
            this.ctx.clearRect(0, 0, SIDES, SIDES);
            this.ctx.beginPath();
            this.ctx.fillStyle = 'white';
            this.squares.forEach(column => column.forEach(square => square.render(this.ctx)));
            this.ctx.fill();
        }

        start() {
            for (let y = 0; y < CELLS; ++y) {
                const row = [];
                for (let x = 0; x < CELLS; ++x) {
                    const r = Math.random();
                    if (r <= 0.03) {
                        row.push(new Square(x * CELL_WH, y * CELL_WH, true));
                    } else row.push(new Square(x * CELL_WH, y * CELL_WH, false));
                }
                this.squares.push(row);
            }

            this.stopped = false;
            const recursiveTimeout = async self => {
                this.render();
                await this.updateKernel();
                if (this.stopped) return;
                self = window.setTimeout(() => recursiveTimeout(self), 200);
            };
            let ptr;
            recursiveTimeout(ptr);
            Game.intervals.push(ptr);
        }

        async updateKernel() {
            try {
                const data = [];
                for (let i = 0; i < CELLS; i++) {
                    let val = 0;
                    for (let j = CELLS; j > 0; j--) {
                        const { alive } = this.squares[i][j - 1];
                        if (alive) val += 1 << j;
                    }
                    data.push(val);
                }
                const answer = await pythonPromise(JSON.stringify(data));
                this.updateData(JSON.parse(answer));
                this.fails = 0;
            } catch (err) {
                console.error(err);
                this.fails++;
                if (this.fails >= 5) {
                    this.stop();
                }
            }
        }

        updateData(data) {
            for (let i = 0; i < CELLS; i++) {
                const num = data[i];
                for (let j = CELLS; j > 0; j--) {
                    const bit = num & (1 << j) ? true : false;
                    this.squares[i][j - 1].alive = bit;
                }
            }
        }

        stop() {
            this.stopped = true;
            window.game = null;
            Game.intervals.forEach(interval => window.clearTimeout(interval));
            Game.intervals = [];
        }
    }

    window.game = new Game();
    window.game.render();
})();
