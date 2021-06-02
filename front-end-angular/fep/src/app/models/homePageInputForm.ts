import { Book } from "./book";

export class HomePageInputForm {



    constructor() {
        this.selectedBook = new Book;
        this.startDate = new Date();
        this.endDate = new Date();
        this.endDate.setDate(this.startDate.getDate() + 5);
        this.culture = 1;
        this.recreation = 1;
        this.nature = 1;
        this.speed = 1;
        this.budget = 2;
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