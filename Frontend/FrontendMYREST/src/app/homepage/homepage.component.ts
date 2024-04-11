import { Component } from '@angular/core';
import { HttpClient } from '@angular/common/http';

@Component({
  selector: 'app-homepage',
  templateUrl: './homepage.component.html',
  styleUrls: ['./homepage.component.scss']
})
export class HomepageComponent {
  menuData!: { [key: string]: { Name: string, Course: string }[] };
  selectedItems: string[] = [];
  menuCategories!: string[];

  constructor(private http: HttpClient) { }

  ngOnInit(): void {
    this.http.get<any>('assets/menu.json').subscribe(data => {
      this.menuData = data;
      this.menuCategories = Object.keys(this.menuData);
    });
  }

  isSelected(item: string): boolean {
    return this.selectedItems.includes(item);
  }

  toggleSelection(item: string) {
    if (this.isSelected(item)) {
      this.selectedItems = this.selectedItems.filter(selectedItem => selectedItem !== item);
    } else {
      this.selectedItems.push(item);
    }
    console.log('Elementos seleccionados:', this.selectedItems);
  }

  enviarSeleccion() {
    console.log('Selección enviada:', this.selectedItems);
  }
  
}
