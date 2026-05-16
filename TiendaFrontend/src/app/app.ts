import { Component, OnInit } from '@angular/core';
import { CommonModule } from '@angular/common';
import { RouterOutlet, RouterLink, RouterLinkActive } from '@angular/router'; // <-- Crítico
import { CarritoService } from './services/carrito';

@Component({
  selector: 'app-root',
  standalone: true,
  imports: [
    CommonModule, 
    RouterOutlet, 
    RouterLink,       // <-- Asegúrate de que esté escrito aquí
    RouterLinkActive  // <-- Asegúrate de que esté escrito aquí
  ],
  templateUrl: './app.html',
  styleUrl: './app.css'
})
export class App implements OnInit {
  title = 'TiendaFrontend';
  contadorCarrito: number = 0;

  constructor(private carritoService: CarritoService) {}

  ngOnInit() {
    this.carritoService.carrito$.subscribe(() => {
      this.contadorCarrito = this.carritoService.obtenerTotalContador();
    });
  }
}