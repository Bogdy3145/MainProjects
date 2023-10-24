import { Component } from '@angular/core';
import { Content } from 'src/app/Content';
import { ContentService } from 'src/app/content.service';
import { Router } from '@angular/router';
import {Location} from '@angular/common';

import { trigger, state, style, animate, transition } from '@angular/animations';


@Component({
  selector: 'app-getcontent',
  templateUrl: './getcontent.component.html',
  styleUrls: ['./getcontent.component.css'],

  
})
export class GetcontentComponent {
  
  
  
  content: Content[] = [];

  constructor(private contentService: ContentService, private location: Location, private router: Router) {}

  ngOnInit() {
    this.getAllContent();
  }

  getAllContent(){
    this.contentService.getAllContent().subscribe(
      (data: any) => {
        this.content = data;
        console.log(this.content);
      }
    );
  }

  refresh(){
    this.contentService.getAllContent().subscribe(
      (data: any) => {
        this.content = data;
        console.log(this.content);
      }
    );
  }


}
