import { Component } from '@angular/core';

@Component({
  selector: 'app-add',
  templateUrl: './add.component.html',
  styleUrls: ['./add.component.css']
})
export class AddComponent {
  book: any = {}; // Assuming you have defined the book object
  showPopup = false;

  handleAdd() {
    if (this.isFormValid()) {
      // Perform the add operation
    } else {
      this.showPopup = true;
    }
  }

  isFormValid(): boolean {
    return (
      this.book.Author &&
      this.book.Title &&
      this.book.Comment &&
      this.book.Date
    );
  }
}
