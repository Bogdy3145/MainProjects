import { Component, OnInit } from '@angular/core';
import { Location } from '@angular/common';

@Component({
  selector: 'app-navigation',
  templateUrl: './navigation.component.html',
  styleUrls: ['./navigation.component.css']
})

export class NavigationComponent implements OnInit {
  protected active: string = 'home';

  constructor(private location: Location) { }

  ngOnInit(): void {
    let url = this.location.path();

    if (url.startsWith('/')) {
      url = url.substring(1);
    }

    if (url.indexOf('/') > -1) {
      url = url.substring(0, url.indexOf('/'));
    }

    this.makeButtonActive(url);
  } 

  makeButtonActive(button: string): void {
    this.active = button;
  }
}
