import { Component } from '@angular/core';
import { Book } from 'src/app/book';
import { BookService } from 'src/app/book.service';

@Component({
  selector: 'app-browse',
  templateUrl: './browse.component.html',
  styleUrls: ['./browse.component.css']
})
export class BrowseComponent {
  books: Book[] = [];
  totalPages: number[] = [];
  currentPage: number = 1;
  filterByAuthor: string = '';
  filterByTitle: string = '';

  constructor(private bookService: BookService) {
    this.currentPage = 1;
  }

  searchBooks() {
    this.currentPage = 1; // Reset current page when performing a new search

    // Call the bookService method to fetch the search results
    this.bookService.getBooks(this.filterByAuthor, this.filterByTitle).subscribe(
      (data: any) => {
        this.books = data.books;
        console.log(this.books);
        this.calculateTotalPages(data.totalPages);
      },
      
    );
  }

  loadPage(page: number, event: Event) {
    event.preventDefault(); // Prevent default anchor tag behavior
  
    // Rest of your code
    if (page === this.currentPage) {
      return; // Do nothing if the requested page is the same as the current page
    }
  
    this.currentPage = page;
  
    // Call the bookService method to fetch the specific page of results
    this.bookService.getBooks(this.filterByAuthor, this.filterByTitle, page).subscribe(
      (data: any) => {
        this.books = data.books;
      },
    );
  }
  

  private calculateTotalPages(nrPages: number) {
    // const itemsPerPage = 3; // Number of books to display per page
    this.totalPages = [];
    // const totalPages = Math.ceil(totalBooks / itemsPerPage);
    for (let i = 1; i <= nrPages; i++) {
      this.totalPages.push(i);
    }
  }
}
