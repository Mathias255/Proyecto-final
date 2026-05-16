import { Routes } from '@angular/router';
import { InicioComponent } from './inicio/inicio'; // Ajusta según tus nombres de archivos
import { ProductosComponent } from './productos/productos';
import { RegistroComponent } from './registro/registro';
import { CarritoComponent } from './carrito/carrito.component'; // <-- Tu nueva factura

export const routes: Routes = [
  { path: 'inicio', component: InicioComponent },
  { path: 'productos', component: ProductosComponent },
  { path: 'registro', component: RegistroComponent },
  { path: 'carrito', component: CarritoComponent }, // <-- Esta línea activa el enlace /carrito
  { path: '', redirectTo: '/inicio', pathMatch: 'full' }
];