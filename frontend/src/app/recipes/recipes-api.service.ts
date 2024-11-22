import {Injectable} from '@angular/core';
import {HttpClient, HttpErrorResponse} from '@angular/common/http';
import {Observable, throwError, catchError} from 'rxjs';
import {API_URL} from '../env';
import {Recipe} from './recipe.model';

@Injectable({providedIn: 'root'})
export class RecipesApiService {

  constructor(private http: HttpClient) {
  }

  private _handleError(err: HttpErrorResponse) {
    return throwError(() => new Error(err.error));
  }

  getRecipes(): Observable<Recipe[]> {
    return this.http
      .get<Recipe[]>(`${API_URL}/recipes`)
      .pipe(catchError(this._handleError));
  }
}