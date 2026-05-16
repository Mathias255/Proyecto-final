import { Component, OnInit } from '@angular/core';
import { CommonModule } from '@angular/common';
import { CarritoService, ItemCarrito } from '../services/carrito';
import { RouterLink } from '@angular/router';

@Component({
  selector: 'app-carrito',
  standalone: true,
  imports: [CommonModule, RouterLink],
  templateUrl: './carrito.component.html',
  styleUrl: './carrito.component.css'
})
export class CarritoComponent implements OnInit {
  items: ItemCarrito[] = [];
  totalPrecio: number = 0;
  fechaActual: Date = new Date();

  constructor(private carritoService: CarritoService) {}

  ngOnInit(): void {
    this.carritoService.carrito$.subscribe(items => {
      this.items = items;
      this.totalPrecio = this.carritoService.obtenerPrecioTotal();
    });
  }

  confirmar() {
    alert('Sincronizando créditos con la Red Nano...\n¡Transacción Exitosa!');
    this.carritoService.limpiarCarrito();
  }
}