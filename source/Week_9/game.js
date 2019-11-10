(() => {
    const SPRITESIZE = 40;
    const SIDES = 600;
    const MAX_RIGHT_BOTTOM = SIDES - SPRITESIZE;
    const SPRITES1 = document.querySelector('#sprites1');
    const SPRITES2 = document.querySelector('#sprites2');

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
        static spriteIndex() {
            const x = Math.floor(Math.random() * 2) * (SPRITES1.width / 3);
            const y = Math.floor(Math.random() * 17) * (SPRITES1.height / 17);
            return { x, y };
        }

        constructor(x, y, angle, spriteX, spriteY, step) {
            if (x) {
                this.x = x;
            } else {
                this.x = Math.random() * MAX_RIGHT_BOTTOM;
            }
            if (y) {
                this.y = y;
            } else {
                this.y = Math.random() * MAX_RIGHT_BOTTOM;
            }
            if (angle) {
                this.angle = angle;
            } else {
                this.angle = Math.random() * 2 * Math.PI;
            }
            if (spriteX && spriteY) {
                this.spriteX = spriteX;
                this.spriteY = spriteY;
            } else {
                const indexes = Square.spriteIndex();
                this.spriteX = indexes.x;
                this.spriteY = indexes.y;
            }
            if (step === 1) {
                this.step = 1;
            } else {
                this.step = 0;
            }
            this.color = randomColor();
        }

        render(ctx) {
            ctx.drawImage(
                this.step ? SPRITES1 : SPRITES2,
                this.spriteX,
                this.spriteY,
                20,
                20,
                this.x,
                this.y,
                SPRITESIZE,
                SPRITESIZE
            );
        }

        move() {
            const newX = this.x + Math.cos(this.angle) * 5;
            const newY = this.y + Math.sin(this.angle) * 5;
            if (newX <= 0 || newX >= MAX_RIGHT_BOTTOM) {
                playSound(BUMPSOUND);
                this.angle += (Math.PI * 3) / 2;
            } else {
                this.x = newX;
            }
            if (newY <= 0 || newY >= MAX_RIGHT_BOTTOM) {
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
            const canvas = document.querySelector('#game');
            this.ctx = canvas.getContext('2d');

            this.stopped = true;
            this.fails = 0;
            this.step = 0;

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
            this.ctx.clearRect(0, 0, SIDES, SIDES);
            this.squares.forEach(square => square.render(this.ctx));
        }

        async move() {
            this.step = this.step ? 0 : 1;

            this.squares.forEach(square => square.move());
            await this.updateKernel();
        }

        start(count) {
            for (let i = 0; i < count; ++i) {
                this.squares.push(new Square());
            }

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
                console.log(answer);
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
            const prevSize = this.squares.length;
            this.squares = data
                .filter(({ deleted }) => !deleted)
                .map(
                    ({ x, y, angle, spriteX, spriteY }) =>
                        new Square(x, y, angle, spriteX, spriteY, this.step)
                );
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

    window.game = new Game();
    window.game.render();
})();
