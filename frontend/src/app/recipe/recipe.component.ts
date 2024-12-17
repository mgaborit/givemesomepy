import { Component, input } from '@angular/core';
import { Recipe } from './recipe.model';
import { MatCardModule } from '@angular/material/card';
import { MatDividerModule } from '@angular/material/divider';

@Component({
  selector: 'app-recipe',
  imports: [MatCardModule, MatDividerModule],
  templateUrl: './recipe.component.html',
  styleUrl: './recipe.component.scss',
})
export class RecipeComponent {
  recipe = input.required<Recipe>();

  constructor() {}
}
