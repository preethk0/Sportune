import React from 'react';
import logo from './logo.svg';
import './App.css';
import './assets/css/main.css';
import image from './assets/css/images/resizedfinallogo.png';

function App() {
  return (
    <div className="App">
      <div id="page-wrapper">


              <div class="inner">
                <header>



                <div className="logoimagebox">
                  <img className="logoimage" src={image} alt="Sportune">
                  </img>
                </div>



                </header>
              </div>
              </div>

          <section class="carousel">
            <div class="reel">

              <article>
                <a href="player_prediction.html" class="image featured"><img src="images/pic02.jpg" alt="" /></a>
                <header>
                  <h3><a href="player_prediction.html">Player Prediction</a></h3>
                </header>
                <p>Get data-driven insights on player salaries. Input a player name and see how much the Sportune model predicts they should get paid!</p>
              </article>

              <article>
                <a href="#" class="image featured"><img src="images/pic03.jpg" alt="" /></a>
                <header>
                  <h3><a href="#">Personal Prediction</a></h3>
                </header>
                <p>Be an NBA player for a day. Input your own statistics and see how much the Sportune model predicts you should get paid!</p>
              </article>

            </div>
          </section>

              </div>
  );
}

export default App;
