import { Component } from '@angular/core';
import { RouterOutlet } from '@angular/router';
import { RecipesApiService } from './recipes/recipes-api.service';
import { Subscription } from 'rxjs';
import { Recipe } from './recipes/recipe.model';

@Component({
  selector: 'app-root',
  standalone: true,
  imports: [RouterOutlet],
  templateUrl: './app.component.html',
  styleUrl: './app.component.scss'
})
export class AppComponent {
  title = 'frontend';
  recipesListSubs?: Subscription;
  recipesList: Recipe[] = [];

  constructor(private recipesApi: RecipesApiService) {}

  ngOnInit() {
    this.recipesListSubs = this.recipesApi
      .getRecipes()
      .subscribe((res: Recipe[]) => {
          this.recipesList = res;
        }
      );
  }

  ngOnDestroy() {
    this.recipesListSubs?.unsubscribe();
  }
}
