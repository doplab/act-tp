(() => {
    const SIDES = 600;
    const CELLS = 32;
    const CELL_WH = SIDES / CELLS;

    class Square {
        constructor(x, y, disabled = 1) {
            this.x = x;
            this.y = y;
            this.disabled = disabled;
        }

        updateState(newState) {
            this.disabled = newState;
        }

        render(ctx) {
            if (!this.disabled) ctx.rect(this.x, this.y, CELL_WH, CELL_WH);
        }
    }

    const pythonPromise = squares =>
        new Promise((resolve, reject) => {
            const callbacks = {
                iopub: {
                    output: data => {
                        try {
                            resolve(data.content.text.split("'").join('"'));
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
            this.ctx.fillStyle = 'white';
            this.squares.forEach(column => column.forEach(square => square.render(this.ctx)));
            this.ctx.fill();
        }

        start() {
            for (let y = -1; y < CELLS + 1; ++y) {
                const row = [];
                for (let x = -1; x < CELLS + 1; ++x) {
                    if (y == CELLS / 2 && x == CELLS / 2)
                        row.push(new Square(x * CELL_WH, y * CELL_WH, 0));
                    else row.push(new Square(x * CELL_WH, y * CELL_WH));
                }
                this.squares.push(row);
            }

            this.stopped = false;
            const renderLoop = async () => {
                this.render();
                if (!this.stopped && this.squares.length > 1)
                    window.requestAnimationFrame(renderLoop);
            };
            window.requestAnimationFrame(renderLoop);
            const recursiveTimeout = async self => {
                await this.updateKernel();
                if (this.stopped) return;
                self = window.setTimeout(() => recursiveTimeout(self), 300);
            };
            let ptr;
            recursiveTimeout(ptr);
            Game.intervals.push(ptr);
        }

        async updateKernel() {
            try {
                const answer = await pythonPromise(JSON.stringify(this.squares));
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
            for (let i = 0; i < CELLS; ++i) {
                for (let j = 0; j < CELLS; ++j) {
                    this.squares[i][j].updateState(data[i][j].disabled ? 1 : 0);
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
