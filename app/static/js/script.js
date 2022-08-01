const navbar = document.getElementById("nav");
const toogle = document.getElementById("toogle");
const nav_links = document.getElementById("nav-links");
const store_side_nav = document.getElementById("store-sidenav");
const profile_dropdown = document.getElementById("acc-store-nav-links");
const profile_section = document.getElementById("nav-user-profile")
const profile_icon = document.getElementById("profile-icon");
const notification = document.getElementById("notification");
const notification_dropdown = document.getElementById("notification-dropdown");
const search_bar = document.getElementById("side-nav-search-bar");
const search_display = document.getElementById("search-display");
const analytics_timeline_toogle = document.getElementById("analtics-timeline-toogle");
const monthly_yearly_analytics = document.getElementById("small-anlytics-card-monthly-yearly");
const hourly_weekly_analytics = document.getElementById("small-anlytics-card-hourly-weekly");
const mobile_search_bar = document.getElementById("side-nav-search-bar-mobile");
const mobile_search_display = document.getElementById("search-display-mobile");
const searchMediaQuery = window.matchMedia("(min-width: 990px)");

document.onclick = function (e) {
  if (e.target.id == "a-nav-link") {
    nav_links.classList.remove("active");
    toogle.classList.remove("active");
  }
};

toogle.onclick = function () {
  toogle.classList.toggle("active");
  if (nav_links) {
    nav_links.classList.toggle("active");
  }
  if (store_side_nav) {
    store_side_nav.classList.toggle("active");
  }
};

if (profile_section) {
  profile_section.onclick = function () {
    if (profile_dropdown) {
      profile_dropdown.classList.toggle("active");
      profile_icon.classList.toggle("active");
    }
  }
};

document.onclick = function (e) {
  if (store_side_nav) {
    if (e.target.id == "nav") {
      store_side_nav.classList.remove("active");
      toogle.classList.remove("active");
    }
  }
};

if (notification) {
  notification.onclick = function () {
    notification_dropdown.classList.toggle("active");
    notification.classList.toggle("active");
  }
}


// function myFunction() {
//   var input, filter, ul, li, a, i, txtValue;
//   input = document.getElementById("side-nav-search-bar");
//   filter = input.value.toUpperCase();
//   ul = document.getElementById("search-display");
//   li = ul.getElementsByTagName("li");

  

//   ul.classList.add("active");

//   for (i = 0; i < li.length; i++) {
//     a = li[i].getElementsByTagName("a")[0];
//     if (a) {
//       console.log(a)
//       txtValue = a.textContent || a.innerText;
//       console.log(txtValue);
//       if (txtValue.toUpperCase().indexOf(filter) > -1) {
//         li[i].style.display = "";
//       } else {
//         ul.innerHTML = "<li>No available search</li>";
//       }
//     }
//   }
// }


// if (search_bar) {
//   document.onclick = function (e) {
//     if (search_display) {
//       if (e.target.id != "side-nav-search-bar") {
//         search_display.classList.remove("active");
//       }
//     }
//   }
// }


if (analytics_timeline_toogle) {
  analytics_timeline_toogle.onclick = function () {
    monthly_yearly_analytics.classList.toggle("active");
    hourly_weekly_analytics.classList.toggle("inactive");
  }
}





function desktopSearchBar() {
  if (search_bar) {
  console.log(search_bar);
  document.onclick = function (e) {
  console.log(search_display);
    if (search_display) {
      if (e.target.id != "side-nav-search-bar") {
        search_display.classList.remove("active");
      } else {
        search_display.classList.add("active");
      }
    }
  };
}
}







function myFunction() {
  var input, filter, ul, li, a, i, txtValue;
  input = document.getElementById("side-nav-search-bar");
  if (searchMediaQuery.matches) {
    input = document.getElementById("side-nav-search-bar");
    ul = document.getElementById("search-display");
    console.log(input);
  } else {
    input = document.getElementById("side-nav-search-bar-mobile");
    ul = document.getElementById("search-display-mobile");
     console.log(input);
  }
  filter = input.value.toUpperCase();
  
  li = ul.getElementsByTagName("li");
 
  // Loop through all list items, and hide those who don't match the search query
  for (i = 0; i < li.length; i++) {
    a = li[i].getElementsByTagName("a")[0];
    txtValue = a.textContent || a.innerText;
    if (txtValue.toUpperCase().indexOf(filter) > -1) {
      li[i].style.display = "";
    } else {
      li[i].style.display = "none";
    }
  }
  ul.style.height = "auto";
}




if (mobile_search_bar) {
  mobile_search_bar.onclick = function () {
    mobile_search_display.classList.toggle("active");
    mobile_search_bar.classList.toggle("active");
  }
}











