import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { AddComponent } from './components/add/add.component';
import { BrowseComponent } from './components/browse/browse.component';
import { UpdateComponent } from './components/update/update.component';
import { DeleteComponent } from './components/delete/delete.component';
import { LoginComponent } from './components/login/login.component';
import { authGuard } from './services/auth.guard';

const routes: Routes = [
  {path: 'addbook', component: AddComponent},
  {path: 'browsebook', component: BrowseComponent},
  {path: 'updatebook', component: UpdateComponent, canActivate: [authGuard] },
  //{path: 'deletebook', component: DeleteComponent},
  { path: 'deletebook', component: DeleteComponent, canActivate: [authGuard] }, // Apply the AuthGuard to delete route
  {path: 'login', component: LoginComponent}
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
