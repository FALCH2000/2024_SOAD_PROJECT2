import { Component } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { MenuService } from '../services/menu.service';

interface MenuItem {
  Name: string;
  Course: string;
}

interface SelectedItems {
  item: MenuItem; // Asigna un número a cada elemento seleccionado
}


@Component({
  selector: 'app-homepage',
  templateUrl: './homepage.component.html',
  styleUrls: ['./homepage.component.scss']
})
export class HomepageComponent {
  menuData!: { [key: string]: MenuItem[] };
  selectedItems: MenuItem[]= [];
  menuCategories!: string[];
  cantidadComidas: string = "1";
  requestDone:boolean = false;
  message:string = "";

  constructor(private menuService:MenuService, private http: HttpClient) { }

  ngOnInit(): void {
    this.http.get<any>('assets/menu.json').subscribe(data => {
      this.menuData = data;
      this.menuCategories = Object.keys(this.menuData);
    });
  }

  isSelected(item: MenuItem) {
    
    
    
  }

  toggleSelection(item: MenuItem) {
    const existe = this.selectedItems.find(selectedItem => selectedItem.Name === item.Name);

    if(existe){
      this.selectedItems = this.selectedItems.filter(selectedItem => selectedItem.Name !== item.Name);
    }else{
      this.selectedItems.push(item);
    }
  }

  enviarSeleccion() {
    console.log(this.cantidadComidas)
    if (this.cantidadComidas === "1") {
      if (Object.keys(this.selectedItems).length > 1) {
        // Deseleccionar todos los elementos checkbox
        const checkboxes = Array.from(document.querySelectorAll<HTMLInputElement>('input[type="checkbox"]'));
        checkboxes.forEach((checkbox: HTMLInputElement) => {
          checkbox.checked = false;
        });
  
        // Vaciar la lista selectedItems
        this.selectedItems = [];

        alert("No puedes enviar mas de 1 seleccion de comida.")
      } else {
        // Enviar selección
        var request = "";

        var item = this.selectedItems[0];
        request += "MealName1="+item.Name+"&CourseType1="+item.Course;
        

        console.log(request)
        this.hacerConsulta(request);
        console.log()
      }
    } else if (this.cantidadComidas === "2") {
      console.log("esteetet")
      if (Object.keys(this.selectedItems).length > 2) {
        // Deseleccionar todos los elementos checkbox
        const checkboxes = Array.from(document.querySelectorAll<HTMLInputElement>('input[type="checkbox"]'));
        checkboxes.forEach((checkbox: HTMLInputElement) => {
          checkbox.checked = false;
        });
  
        // Vaciar la lista selectedItems
        this.selectedItems = [];

        alert("No puedes enviar mas de 1 seleccion de comida.")
      } else {
        // Enviar selección
        var request = "";
        
        var item = this.selectedItems[0];
        request += "MealName1="+item.Name+"&CourseType1="+item.Course;

        var item2 = this.selectedItems[1];
        request += "&MealName2="+item2.Name+"&CourseType2="+item2.Course;

        console.log(request)
        this.hacerConsulta(request);
      }
    }
  
    
  }

  hacerConsulta(entry:string){
    this.menuService.getRecomendacion(entry).subscribe((data)=>{
      console.log(data)
      this.requestDone = true

      console.log(data.data.RecommendedMeals)
      data.data.RecommendedMeals.forEach((meal:any)=>{
        this.message += "Recomendacion: "+meal.Name + " - "+meal.CourseType+"\n"
        console.log(this.message)
      })

      alert(this.message)
    }) 

    
  }
  
}
