import { Injectable } from '@angular/core';
import { BehaviorSubject } from 'rxjs';

export interface ItemCarrito {
  id: number;
  nombre: string;
  precio: number;
  cantidad: number;
}

@Injectable({
  providedIn: 'root'
})
export class CarritoService { 
  private listaCarrito: ItemCarrito[] = [];
  private _carrito = new BehaviorSubject<ItemCarrito[]>([]);
  public carrito$ = this._carrito.asObservable();

  obtenerCarrito() { 
    return this.listaCarrito; 
  }

  agregarProducto(producto: any) {
    const itemExistente = this.listaCarrito.find(item => item.id === producto.id);
    if (itemExistente) {
      itemExistente.cantidad++;
    } else {
      this.listaCarrito.push({
        id: producto.id,
        nombre: producto.nombre,
        precio: producto.precio,
        cantidad: 1
      });
    }
    this._carrito.next([...this.listaCarrito]);
  }

  obtenerTotalContador(): number {
    return this.listaCarrito.reduce((total, item) => total + item.cantidad, 0);
  }

  // AQUÍ ESTÁ LA FUNCIÓN QUE FALTABA RECLAMANDO EL COMPILADOR:
  obtenerPrecioTotal(): number {
    return this.listaCarrito.reduce((total, item) => total + (item.precio * item.cantidad), 0);
  }

  limpiarCarrito() {
    this.listaCarrito = [];
    this._carrito.next([]);
  }
}