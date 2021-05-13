import { Book } from "./book";

export class HomePageInputForm {



    constructor() {
        this.selectedBook = new Book;
        this.startDate = new Date;
        this.endDate = new Date;
        this.culture = 0;
        this.recreation = 0;
        this.nature = 0;
        this.speed = 1;
        this.budget = 1;
    }


    selectedBook: Book;
    startDate: Date;
    endDate: Date;
    culture: number;
    nature: number;
    recreation: number;
    speed: number;
    budget: number;


}