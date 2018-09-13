import { Component, OnInit, ElementRef, ViewChild } from '@angular/core';

@Component({
    selector: 'app-bond-battler-canvas',
    templateUrl: './bond-battler-canvas.component.html',
    styleUrls: ['./bond-battler-canvas.component.css']
})
export class BondBattlerCanvasComponent implements OnInit {

    private canvas: HTMLCanvasElement;

    constructor() { }

    ngOnInit() {
        this.canvas = <HTMLCanvasElement>document.getElementById('bond-battler-canvas');
        
        let drawAndRedraw = (timestampInMs: number) => { };

        drawAndRedraw = (timestampInMs: number) => {
            this.draw();
            requestAnimationFrame(drawAndRedraw);
        };

        requestAnimationFrame(drawAndRedraw);
    }

    draw() {
        let context = this.canvas.getContext('2d');
        const [w,h] = [this.canvas.clientWidth, this.canvas.clientHeight];
        context.clearRect(0, 0, w, h);
        context.fillStyle = "#ddb";
        context.fillRect(0, 0, w, h);
    }

}
