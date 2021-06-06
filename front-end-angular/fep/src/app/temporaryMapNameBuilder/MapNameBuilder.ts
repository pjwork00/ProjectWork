import { HomePageInputForm } from "../models/homePageInputForm";

export class MapNameBuilder {
   
    constructor(){
    }

    buildMapNames(homePageInputForm: HomePageInputForm) : string[]{


        var prefix : string = "../../assets/Maps_saved/Day_";
        var suffix = "_"+homePageInputForm.selectedBook.title
                 +"_CLT_"+homePageInputForm.culture
                 +"_NAT_"+homePageInputForm.nature
                 +"_REC_"+homePageInputForm.recreation
                 +"_SPEED_"+homePageInputForm.speed
                 +"_BUDGET_"+homePageInputForm.budget
                 +"_tot_days_5.html";


       var output : string [] = [prefix+'1'+suffix, prefix+'2'+suffix,prefix+'3'+suffix,prefix+'4'+suffix,prefix+'5'+suffix];

       // Day_1_Angels & Demons_CLT_3_NAT_0_REC_0_SPEED_1_BUDGET_2_tot_days_5.html
       // Day_2_Angels & Demons_CLT_3_NAT_0_REC_0_SPEED_1_BUDGET_2_tot_days_5.html



        return output;
    }

    buildHotelNames(homePageInputForm: HomePageInputForm) : string {
      
        var prefix : string = "../../assets/Maps_saved/";
        var suffix : string = homePageInputForm.selectedBook.title + "_Hotels.html";

        var output : string = prefix+suffix;

        return output;
    }

    buildRestaurantNames(homePageInputForm: HomePageInputForm) : string {
      
        var prefix : string = "../../assets/Maps_saved/";
        var suffix : string = homePageInputForm.selectedBook.title + "_Restaurants.html";

        var output : string = prefix+suffix;

        return output;
    }



}