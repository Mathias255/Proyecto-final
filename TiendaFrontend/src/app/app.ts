import { Component } from '@angular/core';
import { CommonModule } from '@angular/common';
import { RouterOutlet, RouterLink, RouterLinkActive } from '@angular/router';

// Importamos los componentes basándonos en tus pestañas abiertas
import { InicioComponent } from './inicio/inicio'; 
import { ProductosComponent } from './productos/productos';
import { RegistroComponent } from './registro/registro';

@Component({
  selector: 'app-root',
  standalone: true,
  imports: [CommonModule, RouterOutlet, RouterLink, RouterLinkActive],
  templateUrl: './app.html', 
  styleUrl: './app.css' // Asegúrate de que sea .css y no .scss
})
export class App { 
  title = 'TiendaFrontend';
}