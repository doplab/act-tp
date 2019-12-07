(() => {
    const SIDES = 600;
    const CELLS = 30;
    const CELL_WH = SIDES / CELLS;

    class Square {
        constructor(x, y, alive = 1) {
            this.x = x;
            this.y = y;
            this.alive = alive;
        }

        updateState(newState) {
            this.alive = newState;
        }

        render(ctx) {
            if (this.alive) ctx.rect(this.x, this.y, CELL_WH, CELL_WH);
        }
    }

    const pythonPromise = squares =>
        new Promise((resolve, reject) => {
            const callbacks = {
                iopub: {
                    output: data => {
                        try {
                            console.log(data.content.text);
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
            for (let y = 0; y < CELLS; ++y) {
                const row = [];
                for (let x = 0; x < CELLS; ++x) {
                    const r = Math.random();
                    if (r <= 0.03) {
                        row.push(new Square(x * CELL_WH, y * CELL_WH, 1));
                    } else row.push(new Square(x * CELL_WH, y * CELL_WH, 0));
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
                const data = this.squares.map(arr => {
                    let val = 0;
                    arr.forEach((square, index) => {
                        if (square.alive) {
                            val += 1 << (CELLS - index);
                        }
                    });
                    return val;
                });
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
                    this.squares[i][j - 1].updateState(bit);
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
