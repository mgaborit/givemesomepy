import { Component } from '@angular/core';
//import { RouterOutlet } from '@angular/router';
import { RecipesApiService } from './recipe/recipes-api.service';
import { Subscription } from 'rxjs';
import { Recipe } from './recipe/recipe.model';
import { RecipeComponent } from './recipe/recipe.component';
import { CdkAccordionModule } from '@angular/cdk/accordion';

@Component({
  selector: 'app-root',
  imports: [RecipeComponent, CdkAccordionModule /*, RouterOutlet */],
  templateUrl: './app.component.html',
  styleUrl: './app.component.scss',
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
      });
  }

  ngOnDestroy() {
    this.recipesListSubs?.unsubscribe();
  }
}
