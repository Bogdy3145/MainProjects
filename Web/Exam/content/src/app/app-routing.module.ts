import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { GetcontentComponent } from './components/getcontent/getcontent.component';
import { LoginComponent } from './components/login/login.component';
import { AddcontentComponent } from './components/addcontent/addcontent.component';

const routes: Routes = [
  {path: 'content', component: GetcontentComponent},
  {path: 'login', component: LoginComponent},
  {path: 'add', component: AddcontentComponent}
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
