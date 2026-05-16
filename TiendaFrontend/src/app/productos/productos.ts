import { Component, OnInit } from '@angular/core';
import { CommonModule } from '@angular/common';
import { ProductoService } from '../services/producto'; 
import { CarritoService } from '../services/carrito'; // Sube un nivel y entra a services/carrito

@Component({
  selector: 'app-productos',
  standalone: true,
  imports: [CommonModule],
  templateUrl: './productos.html',
  styleUrl: './productos.css'
})
export class ProductosComponent implements OnInit {
  productos: any[] = [];
  productosFiltrados: any[] = [];
  categoriaActual: string = 'Todos';

  constructor(
    private productoService: ProductoService,
    private carritoService: CarritoService // Inyección del servicio del carrito
  ) {}

  ngOnInit(): void {
    this.cargarProductos();
  }

  cargarProductos() {
    this.productoService.getProductos().subscribe({
      next: (data: any) => {
        this.productos = data;
        this.productosFiltrados = data;
      },
      error: (err: any) => console.error('Error de conexión:', err)
    });
  }

  filtrar(categoria: string) {
    this.categoriaActual = categoria;
    if (categoria === 'Todos') {
      this.productosFiltrados = this.productos;
    } else {
      this.productosFiltrados = this.productos.filter(p => p.categoria === categoria);
    }
  }

  // Ejecuta la función del servicio enviando el producto seleccionado
  adquirir(producto: any) {
    this.carritoService.agregarProducto(producto);
  }
}