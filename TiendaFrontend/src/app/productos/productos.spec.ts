import { ComponentFixture, TestBed } from '@angular/core/testing';
import { ProductosComponent } from './productos'; // <-- Corregido el nombre de la clase importada
import { ProductoService } from '../services/producto';
import { CarritoService } from '../services/carrito';
import { provideHttpClient } from '@angular/common/http'; // Crítico para que no falle por falta de HTTP

describe('ProductosComponent', () => {
  let component: ProductosComponent;
  let fixture: ComponentFixture<ProductosComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [ProductosComponent], // <-- Se usa el nombre real del componente standalone
      providers: [
        ProductoService,
        CarritoService,
        provideHttpClient() // Inyecta la simulación de servicios de red
      ]
    }).compileComponents();

    fixture = TestBed.createComponent(ProductosComponent);
    component = fixture.componentInstance;
    fixture.detectChanges(); // Ejecuta los ciclos de vida como el ngOnInit
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});