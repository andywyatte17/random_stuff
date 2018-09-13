import {
  Component,
  OnInit,
  ElementRef,
  ViewChild,
  HostListener
} from "@angular/core";

enum KeyCode {
  ArrowDown = 0x28,
  ArrowLeft = 0x25,
  ArrowRight = 0x27,
  ArrowUp = 0x26,
  Space = 0x20
}

@Component({
  selector: "app-bond-battler-canvas",
  templateUrl: "./bond-battler-canvas.component.html",
  styleUrls: ["./bond-battler-canvas.component.css"]
})
export class BondBattlerCanvasComponent implements OnInit {
  private canvas: HTMLCanvasElement;

  constructor() {}

  ngOnInit() {
    this.canvas = <HTMLCanvasElement>(
      document.getElementById("bond-battler-canvas")
    );

    this.onResizeImpl();
    this.setupDrawingLoop();
  }

  private setupDrawingLoop() {
    let drawAndRedraw = (timestampInMs: number) => {};

    let last = 0;
    drawAndRedraw = (timestampInMs: number) => {
      if (timestampInMs > last + 100) {
        last = timestampInMs;
        this.draw();
      }
      requestAnimationFrame(drawAndRedraw);
    };

    requestAnimationFrame(drawAndRedraw);
  }

  private targetter: number = null;
  private bonds = [4, 5, 6, 7];
  private whichBond = 0;

  private bondRect(
    bondIndex: number,
    boundCount: number,
    w: number,
    h: number
  ) {
    // spacing + bond_1 + spacing + bond_2 + ... + spacing
    // (n+1)*spacing + n*bond_width = w
    // bond_width = (w - (n+1)*spacing)/n
    const spacing = 10;
    const height = Math.max(50, h / 100.0);
    const n = boundCount;
    const bond_width = (w - (n + 1) * spacing) / n;
    return {
      x: (spacing + bond_width) * (bondIndex + 1) - bond_width,
      y: spacing,
      w: bond_width,
      h: height
    };
  }

  private onResizeImpl() {
    this.canvas.style.width = "100%";
    let h = window.innerHeight - this.canvas.offsetTop - 30;
    this.canvas.style.height = `${h}px`;
    // ...then set the internal size to match
    this.canvas.width = this.canvas.offsetWidth;
    this.canvas.height = this.canvas.offsetHeight;
  }

  @HostListener("window:resize", ["$event"])
  private onResize(event) {
    this.onResizeImpl();
  }

  @HostListener("window:keydown", ["$event"])
  private onkeydown(event: Event) {
    let e2 = <KeyboardEvent>event;
    let lock = () => {
      this.whichBond = Math.max(
        Math.min(this.bonds.length - 1, this.whichBond),
        0
      );
    };
    switch (<KeyCode>e2.keyCode) {
      case KeyCode.ArrowLeft:
        this.whichBond = this.whichBond - 1;
        lock();
        break;
      case KeyCode.ArrowRight:
        this.whichBond = this.whichBond + 1;
        lock();
        break;
      case KeyCode.Space:
        break;
    }
    event.preventDefault();
  }

  draw() {
    let context = this.canvas.getContext("2d");
    const [w, h] = [this.canvas.offsetWidth, this.canvas.offsetHeight];
    context.clearRect(0, 0, w, h);
    context.fillStyle = "#ddb";
    context.fillRect(0, 0, w, h);
    context.font = "20px sans-serif Arial";
    this.bonds.forEach((bond: number, index: number) => {
      const r = this.bondRect(index, this.bonds.length, w, h);
      context.fillStyle = index === this.whichBond ? "#dbb" : "#bdb";
      context.fillRect(r.x, r.y, r.w, r.h);
      context.fillStyle = "rgba(0,0,0,0.9)";
      context.fillText(`${bond}`, r.x + r.w * 0.5, r.y + r.h * 0.5);
    });
  }
}
