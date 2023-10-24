import { Component } from '@angular/core';
import { ContentService } from 'src/app/content.service';
import { Content } from 'src/app/Content';
import { Router } from '@angular/router';
import {Location} from '@angular/common';

@Component({
  selector: 'app-addcontent',
  templateUrl: './addcontent.component.html',
  styleUrls: ['./addcontent.component.css']
})
export class AddcontentComponent {
  content: any = {}; // Assuming you have defined the book object
  showPopup = false;

  localContent: Content = { Title: '', Description: '', Url: '', Date:0, UserId:0, Id:0 };

  constructor(private contentService: ContentService, private location: Location, private router: Router) {}


  

  handleAdd() {
    console.log(localStorage.getItem('role'));
    if (localStorage.getItem('role')=="creator"){

    console.log(this.localContent);
    if (this.isFormValid()) {
      const uid = localStorage.getItem('userid');
      if (uid){
        this.localContent.UserId = parseInt(uid);
      }

      this.localContent.Date = 2099;

      this.contentService.addContent(this.localContent).subscribe(
        (response) => {
          console.log(this.localContent);
          console.log('Add successful:', response);
          
          this.router.navigate(['/content']);

          //this.location.go(this.location.path()); // Reload the current URL
          //window.location.reload(); // Reload the entire page
          // Handle success, e.g., show a success message or navigate to another page
        }
        
      );
      // Perform the add operation
    } else {
      this.showPopup = true;
    }
  }
  }

  isFormValid(): boolean {
    return (
      this.localContent.Title != '' &&
      this.localContent.Description != '' &&
      this.localContent.Url != '' 
    );
  }
}
