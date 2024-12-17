import { Difficulty } from './difficulty.enum';

export class Recipe {
  constructor(
    public name: string,
    public difficulty: Difficulty,
    public time: number
  ) {}
}
