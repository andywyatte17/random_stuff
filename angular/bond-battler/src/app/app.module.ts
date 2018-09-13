import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';


import { AppComponent } from './app.component';
import { BondBattlerCanvasComponent } from './bond-battler-canvas/bond-battler-canvas.component';


@NgModule({
  declarations: [
    AppComponent,
    BondBattlerCanvasComponent
  ],
  imports: [
    BrowserModule
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
