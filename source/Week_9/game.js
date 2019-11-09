(() => {
    const randomColor = () => {
        return `rgb(${Math.random() * 255}, ${Math.random() * 255}, ${Math.random() * 255})`;
    };

    const BUMPSOUND = 'https://themushroomkingdom.net/sounds/wav/smb/smb_bump.wav';
    const SMASHSOUND = 'https://themushroomkingdom.net/sounds/wav/smb/smb_breakblock.wav';
    const FINISHSOUND = 'https://themushroomkingdom.net/sounds/wav/smb/smb_stage_clear.wav';

    const playSound = name => {
        var sound = new Audio(name);
        sound.play();
    };

    class Square {
        constructor(x, y, angle) {
            if (x) {
                this.x = x;
            } else {
                this.x = Math.random() * 380;
            }
            if (y) {
                this.y = y;
            } else {
                this.y = Math.random() * 380;
            }
            if (angle) {
                this.angle = angle;
            } else {
                this.angle = Math.random() * 2 * Math.PI;
            }
            this.color = randomColor();
        }

        render(ctx) {
            ctx.beginPath();
            ctx.strokeStyle = this.color;
            ctx.fillStyle = this.color;
            ctx.rect(this.x, this.y, 20, 20);
            ctx.stroke();
            ctx.fill();
        }

        move() {
            const newX = this.x + Math.cos(this.angle) * 5;
            const newY = this.y + Math.sin(this.angle) * 5;
            if (newX <= 0 || newX >= 380) {
                playSound(BUMPSOUND);
                this.angle += (Math.PI * 3) / 2;
            } else {
                this.x = newX;
            }
            if (newY <= 0 || newY >= 380) {
                playSound(BUMPSOUND);
                this.angle += (Math.PI * 3) / 2;
            } else {
                this.y = newY;
            }
        }
    }

    const pythonPromise = squares =>
        new Promise((resolve, reject) => {
            const callbacks = {
                iopub: {
                    output: data => {
                        try {
                            resolve(JSON.parse(data.content.text.split("'").join('"')));
                        } catch (err) {
                            reject(err);
                        }
                    }
                }
            };
            IPython.notebook.kernel.execute(`Binder.instance.update_data(${squares})`, callbacks);
        });

    class Game {
        constructor(count, canvas) {
            this.squares = [];
            this.ctx = canvas.getContext('2d');
            for (let i = 0; i < count; ++i) {
                this.squares.push(new Square());
            }

            this.stopped = true;
            this.fails = 0;

            if (!Game.intervals) Game.intervals = [];
            else {
                Game.intervals.forEach(interval => window.clearTimeout(interval));
                Game.intervals = [];
            }

            this.move = this.move.bind(this);
            this.render = this.render.bind(this);
            this.start = this.start.bind(this);
            this.updateData = this.updateData.bind(this);
            this.updateKernel = this.updateKernel.bind(this);
            this.stop = this.stop.bind(this);
        }

        render() {
            this.ctx.clearRect(0, 0, 400, 400);
            this.squares.forEach(square => square.render(this.ctx));
        }

        async move() {
            this.squares.forEach(square => square.move());
            await this.updateKernel();
        }

        start() {
            this.stopped = false;
            const renderLoop = () => {
                this.render();
                if (!this.stopped && this.squares.length > 1)
                    window.requestAnimationFrame(renderLoop);
                else if (this.squares.length <= 1) {
                    playSound(FINISHSOUND);
                    this.stop();
                }
            };
            window.requestAnimationFrame(renderLoop);
            const recursiveTimeout = async self => {
                await this.move();
                if (this.stopped) return;
                self = window.setTimeout(() => recursiveTimeout(self), 25);
            };
            let ptr;
            recursiveTimeout(ptr);
            Game.intervals.push(ptr);
        }

        async updateKernel() {
            try {
                const answer = await pythonPromise(JSON.stringify(this.squares));
                //console.log(anwer);
                this.updateData(answer);
                this.fails = 0;
            } catch (err) {
                this.fails++;
                if (this.fails >= 5) {
                    this.stop();
                }
            }
        }

        updateData(data) {
            const prevSize = this.squares.length;
            this.squares = data
                .filter(({ deleted }) => !deleted)
                .map(({ x, y, angle }) => new Square(x, y, angle));
            if (this.squares.length != prevSize) {
                playSound(SMASHSOUND);
            }
        }

        stop() {
            this.stopped = true;
            window.game = null;
            Game.intervals.forEach(interval => window.clearTimeout(interval));
            Game.intervals = [];
        }
    }

    const canvas = document.querySelector('#game');
    window.game = new Game(5, canvas);
    window.game.render();
})();
