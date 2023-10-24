import { ComponentFixture, TestBed } from '@angular/core/testing';

import { GetcontentComponent } from './getcontent.component';

describe('GetcontentComponent', () => {
  let component: GetcontentComponent;
  let fixture: ComponentFixture<GetcontentComponent>;

  beforeEach(() => {
    TestBed.configureTestingModule({
      declarations: [GetcontentComponent]
    });
    fixture = TestBed.createComponent(GetcontentComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
