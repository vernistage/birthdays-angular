import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'app-events',
  templateUrl: './events.component.html',
  styleUrls: ['./events.component.css']
})
export class EventsComponent implements OnInit {

  event = Event = {
    id: 1,
    title: "Event 1",
    description: "First event",
    address: "at the house",
    start_time: "October 5",
    end_time: "November 5",
  };

  constructor() { }

  ngOnInit() {
  }

}
