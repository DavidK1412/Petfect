<template>
  <div>
    <header class="header">
      <div class="container">
        <div class="header-box">
          <a href="#home">
            <img src="../assets/header_logo.svg" alt="logo">
          </a>
          <nav ref="nav" class="header_nav">
            <ul class="header_nav-list">
              <li class="header_nav-item" v-on:click="toggleMenu"><a href="#home">Inicio</a></li>
              <li class="header_nav-item" v-on:click="toggleMenu"><a href="#about">Sobre Nosotros</a></li>
              <li class="header_nav-item" v-on:click="toggleMenu"><a href="#services">Servicios</a></li>
              <li class="header_nav-item" v-on:click="toggleMenu"><a href="#experiences">Experiencias</a></li>
              <li class="header_nav-item" v-on:click="toggleMenu"><button @click="togglePopUp">Agendar</button></li>
            </ul>
            <button ref="mobileMenu" v-on:click="toggleMenu"  class="mobile-menu" aria-expanded="false" aria-label="Abrir menu">
              <span class="mobile-menu_line-1"></span>
              <span class="mobile-menu_line-2"></span>
              <span class="mobile-menu_line-3"></span>
            </button>
          </nav>
        </div>
      </div>
    </header>

    <main class="main">
      <div class="container">
        <section id="home" class="hero">
          <div class="hero_content">
            <transition name="fade">
              <LogInPopUp v-show="popUp" @close="togglePopUp"/>
            </transition>
            <header>
              <h1>
                El <span class="hero_purple">mejor spa <img class="hero_detail" src="../assets/hero_detalle.svg" width="45" height="45"></span><br> para tu mascota.
              </h1>
            </header>
            <p>El trato que ellos merecen ❤️.</p>
            <button class="main_btn" @click="togglePopUp">¡Agenda con nosotros!</button>
          </div>
          <picture>
            <source media="(max-width: 1170px)" srcset="../assets/hero_mobileImg.jpg">
            <img class="hero_img" src="../assets/hero_img.jpg" alt="Golden retriever">
          </picture>
        </section>
        <section id="about" class="sobre">
          <picture class="sobre_img">
            <source media="(max-width: 600px)" srcset="../assets/sobre_img.jpg">
            <source media="(max-width: 1170px)" srcset="../assets/sobre_mobileImg.jpg">
            <img src="../assets/sobre_img.jpg" alt="Foto de un perro y un gato">
          </picture>
          <div class="sobre_content">
            <header>
              <h2>Sobre <span class="sobre_detail">Nosotros <img src="../assets/main_detalle.svg" alt="" width="30" height="31"></span></h2>
            </header>
            <p>
              ¡Bienvenidos al oasis de relajación y cuidado para sus queridos amigos de cuatro patas! En nuestro Spa para Mascotas, entendemos que su compañero peludo es más que una mascota; es un miembro de la familia. Por eso, ofrecemos una experiencia de spa de lujo donde cada mascota es tratada con el amor y la atención que merece. Desde masajes relajantes hasta tratamientos de belleza personalizados, nuestro equipo de profesionales capacitados se dedica a proporcionar un servicio excepcional en un ambiente sereno y acogedor. ¡Permita que su mascota disfrute de un día de mimos y salga luciendo y sintiéndose mejor que nunca!
            </p>
          </div>
        </section>
        <section class="info">
          <div class="container">
            <ul class="info-box">
              <li class="info_card">
                <img src="../assets/icon_profesionales.svg" alt="" width="90" height="90">
                <p><span class="info_purple">20+</span><br>Profesionales</p>
              </li>
              <li class="info_card">
                <img src="../assets/icon_clientes.svg" alt="" width="90" height="90">
                <p><span class="info_purple">5000+</span><br>Clientes felices</p>
              </li>
              <li class="info_card">
                <img src="../assets/icon_premios.svg" alt="" width="90" height="90">
                <p><span class="info_purple">20+</span><br>Certificaciones</p>
              </li>
              <li class="info_card">
                <img src="../assets/icon_mercado.svg" alt="" width="90" height="90">
                <p><span class="info_purple">8+</span><br>Años haciendo lo que nos gusta</p>
              </li>
            </ul>
          </div>
        </section>
        <div class="container">
          <section id="services" class="services">
            <header class="services_title">
              <h2>
                <span class="services_detail main_detail">
                  Servicios <img src="../assets/main_detalle-esq.svg" alt="" width="30" height="31">
                </span>  que ofrecemos
              </h2>
              <p>
                Nuestro Spa para Mascotas ofrece una amplia gama de servicios de spa de lujo para satisfacer las necesidades de su mascota. Desde masajes relajantes hasta tratamientos de belleza personalizados, nuestro equipo de profesionales capacitados se dedica a proporcionar un servicio excepcional en un ambiente sereno y acogedor.
              </p>
            </header>
            <ul class="services_content">
              <li class="services_card">
                <img src="../assets/servicos_banio.svg" alt="" width="80" height="82">
                <div class="services_card-content">
                    <h3>Baño</h3>
                    <p>¡Dale a tu mascota un baño de lujo! Nuestros baños de spa incluyen un baño relajante con champú y acondicionador de alta calidad, seguido de un secado suave y un cepillado completo.</p>
                </div>
              </li>
              <li class="services_card">
                <img src="../assets/servicos_corte.svg" alt="" width="80" height="82">
                <div class="services_card-content">

                    <h3>Corte</h3>
                    <p>¡Haz que tu mascota luzca y se sienta mejor que nunca! Nuestros servicios de corte de lujo incluyen un baño relajante, un corte de pelo personalizado y un cepillado completo.</p>
                </div>
              </li>
              <li class="services_card services_card-host">
                <img src="../assets/servicos_hospedaje.svg" alt="" width="80" height="82">
                <div class="services_card-contenido">
                  <h3>Hospedaje</h3>
                  <p>¡Deje a su mascota en buenas manos! Nuestro servicio de hospedaje de lujo incluye una habitación privada y cómoda, paseos diarios y mucho amor y atención de nuestro personal amable y atento.</p>
                </div>
              </li>
              <li class="services_card">
                <img src="../assets/servicos_clinica.svg" alt="" width="80" height="82">
                <div class="services_card-content">

                    <h3>Veterinaria</h3>
                    <p>¡Mantén a tu mascota sana y feliz! Nuestros servicios veterinarios incluyen exámenes de bienestar, vacunas, desparasitación y mucho más para garantizar la salud y el bienestar de tu mascota.</p>
                </div>
              </li>
            </ul>
          </section>
          <article id="experiences" class="experiences">
            <header class="experiences_title">
              <h2>
                <span class="experiences_detail main_detail">
                  Experiencias <img src="../assets/main_detalle-esq.svg" alt="" width="30" height="31">
                </span>  de nuestros clientes
              </h2>
              <p>
                Nuestro Spa para Mascotas se dedica a proporcionar una experiencia de spa de lujo donde cada mascota es tratada con el amor y la atención que merece. ¡Descubre lo que nuestros clientes satisfechos tienen que decir sobre nosotros!
              </p>
            </header>
            <div class="experiences_content">
              <ul ref="slider" class="experiences_slider">
                <li class="experiences_card">
                  <img src="../assets/experiencias_img1.jpg" alt="" class="experiences_persons" width="200" height="200">
                  <div class="experiences_card-content">
                    <h3>
                      Bruno
                    </h3>
                    <h4>
                      Golden Retriever
                    </h4>
                    <p>
                      "¡Mi mascota siempre sale feliz y relajada de su día de spa en este lugar! El personal es amable y atento"
                    </p>
                    <br>
                    <img src="../assets/experiencias_5estrellas.svg" alt="" width="190"
                         height="30">
                  </div>
                </li>
                <li class="experiences_card">
                  <img src="../assets/experiencias_img2.jpg" alt="" class="experiences_persons" width="200" height="200">
                  <div class="experiences_card-content">
                    <h3>
                      Laika
                    </h3>
                    <h4>
                      Criollita
                    </h4>
                    <p>
                      "¡Mi mascota siempre sale feliz y relajada de su día de spa en este lugar! El personal es amable y atento"
                    </p>
                    <br>
                    <img src="../assets/experiencias_5estrellas.svg" alt="" width="190"
                         height="30">
                  </div>
                </li>
                <li class="experiences_card">
                  <img src="../assets/experiencias_img3.jpg" alt="" class="experiences_persons" width="200" height="200">
                  <div class="experiences_card-content">
                    <h3>
                      Candy
                    </h3>
                    <h4>
                      Gata criolla
                    </h4>
                    <p>
                      "¡Mi mascota siempre sale feliz y relajada de su día de spa en este lugar! El personal es amable y atento"
                    </p>
                    <br>
                    <img src="../assets/experiencias_4extrellas.svg" alt="" width="190"
                         height="30">
                  </div>
                </li>
                <li class="experiences_card">
                  <img src="../assets/experiencias_img1.jpg" alt="" class="experiences_persons" width="200" height="200">
                  <div class="experiences_card-content">
                    <h3>
                      Bruno
                    </h3>
                    <h4>
                      Golden Retriever
                    </h4>
                    <p>
                      "¡Mi mascota siempre sale feliz y relajada de su día de spa en este lugar! El personal es amable y atento"
                    </p>
                    <br>
                    <img src="../assets/experiencias_5estrellas.svg" alt="" width="190"
                         height="30">
                  </div>
                </li>
                <li class="experiences_card">
                  <img src="../assets/experiencias_img2.jpg" alt="" class="experiences_persons" width="200" height="200">
                  <div class="experiences_card-content">
                    <h3>
                      Laika
                    </h3>
                    <h4>
                      Criollita
                    </h4>
                    <p>
                      "¡Mi mascota siempre sale feliz y relajada de su día de spa en este lugar! El personal es amable y atento"
                    </p>
                    <br>
                    <img src="../assets/experiencias_5estrellas.svg" alt="" width="190"
                         height="30">
                  </div>
                </li>
                <li class="experiences_card">
                  <img src="../assets/experiencias_img3.jpg" alt="" class="experiences_persons" width="200" height="200">
                  <div class="experiences_card-content">
                    <h3>
                      Candy
                    </h3>
                    <h4>
                      Gata criolla
                    </h4>
                    <p>
                      "¡Mi mascota siempre sale feliz y relajada de su día de spa en este lugar! El personal es amable y atento"
                    </p>
                    <br>
                    <img src="../assets/experiencias_4extrellas.svg" alt="" width="190"
                         height="30">
                  </div>
                </li>
              </ul>
              <div class="indicador" ref="indicators">
                <button v-on:click="changeSlide(0)" aria-label="indicador número 1" class="indicador_btn active">&nbsp;</button>
                <button v-on:click="changeSlide(1)" aria-label="indicador número 2" class="indicador_btn">&nbsp;</button>
                <button v-on:click="changeSlide(2)" aria-label="indicador número 3" class="indicador_btn">&nbsp;</button>
                <button v-on:click="changeSlide(3)" aria-label="indicador número 4" class="indicador_btn indicador_btn-extra">&nbsp;</button>
                <button v-on:click="changeSlide(4)" aria-label="indicador número 5" class="indicador_btn indicador_btn-extra">&nbsp;</button>
                <button v-on:click="changeSlide(5)" aria-label="indicador número 6" class="indicador_btn indicador_btn-extra">&nbsp;</button>
              </div>
            </div>
          </article>
          <section class="client_service">
            <div class="client_service-box">
              <div class="client_service-content">
                <header>
                  <h2>Horarios de atención</h2>
                </header>
                <span class="line">&nbsp;</span>
                <div class="client_service-schedules">
                  <p>Lunes a Viernes</p>
                  <p>7:00 am - 11:00 pm</p>
                </div>
                <div class="client_service-schedules">
                  <p>Sábados, Domingos y Festivos</p>
                  <p>7:00 am - 5:00 pm</p>
                </div>
              </div>
              <div class="client_service_image">
                <img src="../assets/servicio.png" alt="">
              </div>
            </div>
          </section>
        </div>
      </div>
    </main>
    <footer class="footer">
      <div class="container">
        <div class="footer-box">
          <nav class="footer_social">
            <a href="#home">
              <img class="footer_logo" src="../assets/footer_logo.svg" alt="" width="180" height="72">
            </a>
            <ul class="media">
              <li><a href="#"><svg width="45" height="50" viewBox="0 0 45 50" fill="none"
                                   xmlns="http://www.w3.org/2000/svg">
                <g clip-path="url(#clip0_27_5289)">
                  <path
                      d="M22.5 19.791C21.4404 19.7914 20.4047 20.0972 19.5239 20.6698C18.6431 21.2424 17.9567 22.0561 17.5515 23.008C17.1462 23.9598 17.0404 25.0071 17.2474 26.0174C17.4543 27.0277 17.9648 27.9557 18.7142 28.684C19.4636 29.4123 20.4182 29.9082 21.4575 30.109C22.4967 30.3099 23.5739 30.2066 24.5528 29.8123C25.5317 29.418 26.3684 28.7503 26.957 27.8938C27.5456 27.0372 27.8598 26.0302 27.8598 25C27.8588 23.6185 27.2937 22.2939 26.2887 21.3171C25.2837 20.3404 23.921 19.7915 22.5 19.791ZM35.0267 15.7871C34.7539 15.1151 34.342 14.5047 33.8166 13.9939C33.2911 13.483 32.6633 13.0826 31.9721 12.8174C29.8627 12.0078 24.8404 12.1895 22.5 12.1895C20.1596 12.1895 15.1423 12.001 13.0269 12.8174C12.3357 13.0826 11.7079 13.483 11.1824 13.9939C10.657 14.5047 10.2451 15.1151 9.97232 15.7871C9.14062 17.8379 9.32645 22.7256 9.32645 24.999C9.32645 27.2725 9.14062 32.1543 9.97634 34.2119C10.2491 34.8839 10.661 35.4943 11.1864 36.0052C11.7119 36.516 12.3397 36.9165 13.0309 37.1816C15.1403 37.9912 20.1626 37.8096 22.504 37.8096C24.8454 37.8096 29.8607 37.998 31.9761 37.1816C32.6673 36.9165 33.2952 36.516 33.8206 36.0052C34.3461 35.4943 34.7579 34.8839 35.0307 34.2119C35.8694 32.1611 35.6766 27.2734 35.6766 25C35.6766 22.7266 35.8694 17.8457 35.0307 15.7881L35.0267 15.7871ZM22.5 33.0078C20.871 33.0078 19.2785 32.5382 17.924 31.6583C16.5695 30.7783 15.5138 29.5277 14.8904 28.0645C14.267 26.6012 14.1038 24.9911 14.4217 23.4378C14.7395 21.8844 15.5239 20.4575 16.6758 19.3376C17.8277 18.2177 19.2954 17.455 20.8931 17.1461C22.4909 16.8371 24.147 16.9957 25.652 17.6017C27.1571 18.2078 28.4434 19.2342 29.3485 20.5511C30.2535 21.868 30.7366 23.4162 30.7366 25C30.7379 26.052 30.5258 27.0938 30.1123 28.066C29.6989 29.0381 29.0922 29.9214 28.3271 30.6652C27.562 31.4091 26.6535 31.9989 25.6536 32.4009C24.6537 32.8028 23.582 33.0091 22.5 33.0078ZM31.0761 18.5254C30.6958 18.5256 30.324 18.4161 30.0077 18.2109C29.6914 18.0056 29.4449 17.7137 29.2992 17.3722C29.1535 17.0307 29.1153 16.6548 29.1894 16.2922C29.2635 15.9296 29.4465 15.5964 29.7153 15.3349C29.9841 15.0734 30.3267 14.8953 30.6997 14.8231C31.0726 14.7509 31.4592 14.7879 31.8106 14.9293C32.162 15.0707 32.4623 15.3103 32.6736 15.6177C32.8849 15.9251 32.9977 16.2865 32.9977 16.6562C32.9987 16.9018 32.9499 17.1451 32.854 17.3722C32.7581 17.5994 32.6171 17.8059 32.4389 17.9799C32.2608 18.1539 32.049 18.292 31.8159 18.3863C31.5827 18.4806 31.3327 18.5292 31.0801 18.5293L31.0761 18.5254ZM40.1786 3.125H4.82143C3.54271 3.125 2.31636 3.61886 1.41216 4.49794C0.50797 5.37701 0 6.5693 0 7.8125L0 42.1875C0 43.4307 0.50797 44.623 1.41216 45.5021C2.31636 46.3811 3.54271 46.875 4.82143 46.875H40.1786C41.4573 46.875 42.6836 46.3811 43.5878 45.5021C44.492 44.623 45 43.4307 45 42.1875V7.8125C45 6.5693 44.492 5.37701 43.5878 4.49794C42.6836 3.61886 41.4573 3.125 40.1786 3.125ZM38.4589 31.4453C38.3294 33.9482 37.7417 36.166 35.8624 37.9883C33.983 39.8105 31.7039 40.3936 29.1325 40.5127C26.4797 40.6582 18.5263 40.6582 15.8735 40.5127C13.2991 40.3867 11.026 39.8145 9.14364 37.9883C7.26127 36.1621 6.66964 33.9434 6.5471 31.4453C6.39743 28.8652 6.39743 21.1318 6.5471 18.5547C6.67667 16.0518 7.25725 13.834 9.14364 12.0117C11.03 10.1895 13.3092 9.61328 15.8735 9.49414C18.5263 9.34863 26.4797 9.34863 29.1325 9.49414C31.7069 9.62012 33.9871 10.1924 35.8624 12.0186C37.7377 13.8447 38.3364 16.0635 38.4589 18.5664C38.6086 21.1367 38.6086 28.8633 38.4589 31.4453Z"
                      fill="#A55BF0" />
                </g>
                <defs>
                  <clipPath id="clip0_27_5289">
                    <rect width="45" height="50" fill="white" />
                  </clipPath>
                </defs>
              </svg>
              </a>

              </li>
              <li><a href="#"><svg width="45" height="50" viewBox="0 0 45 50" fill="none"
                                   xmlns="http://www.w3.org/2000/svg">
                <path
                    d="M40.1786 3.125H4.82143C2.1596 3.125 0 5.22461 0 7.8125V42.1875C0 44.7754 2.1596 46.875 4.82143 46.875H40.1786C42.8404 46.875 45 44.7754 45 42.1875V7.8125C45 5.22461 42.8404 3.125 40.1786 3.125ZM35.2667 18.6328C35.2868 18.9062 35.2868 19.1895 35.2868 19.4629C35.2868 27.9297 28.6574 37.6855 16.5435 37.6855C12.8069 37.6855 9.34152 36.6309 6.42857 34.8145C6.96094 34.873 7.47321 34.8926 8.01562 34.8926C11.0993 34.8926 13.9319 33.877 16.192 32.1582C13.2991 32.0996 10.8683 30.2539 10.0346 27.7148C11.0491 27.8613 11.9632 27.8613 13.0078 27.5977C9.99442 27.002 7.73437 24.4238 7.73437 21.3086V21.2305C8.60826 21.709 9.63281 22.002 10.7076 22.041C9.804 21.4567 9.06326 20.6639 8.55148 19.7335C8.03969 18.8032 7.77278 17.7641 7.77455 16.709C7.77455 15.5176 8.09598 14.4238 8.66853 13.4766C11.9129 17.3633 16.7846 19.9023 22.2489 20.1758C21.3147 15.8301 24.6596 12.3047 28.6775 12.3047C30.5759 12.3047 32.2835 13.0762 33.4888 14.3262C34.9754 14.0527 36.4018 13.5156 37.6674 12.7832C37.1752 14.2676 36.1406 15.5176 34.7746 16.3086C36.1004 16.1719 37.3862 15.8105 38.5714 15.3125C37.6775 16.5918 36.5525 17.7246 35.2667 18.6328Z"
                    fill="#A55BF0" />
              </svg>
              </a>
              </li>
              <li><a href="#"><svg width="45" height="50" viewBox="0 0 45 50" fill="none"
                                   xmlns="http://www.w3.org/2000/svg">
                <g clip-path="url(#clip0_27_5293)">
                  <path
                      d="M40.1786 3.125H4.82143C3.54271 3.125 2.31636 3.61886 1.41216 4.49794C0.50797 5.37701 0 6.5693 0 7.8125L0 42.1875C0 43.4307 0.50797 44.623 1.41216 45.5021C2.31636 46.3811 3.54271 46.875 4.82143 46.875H18.6077V32.001H12.2796V25H18.6077V19.6641C18.6077 13.5947 22.3242 10.2422 28.0165 10.2422C30.7426 10.2422 33.5933 10.7148 33.5933 10.7148V16.6719H30.4523C27.3576 16.6719 26.3923 18.5391 26.3923 20.4541V25H33.301L32.1961 32.001H26.3923V46.875H40.1786C41.4573 46.875 42.6836 46.3811 43.5878 45.5021C44.492 44.623 45 43.4307 45 42.1875V7.8125C45 6.5693 44.492 5.37701 43.5878 4.49794C42.6836 3.61886 41.4573 3.125 40.1786 3.125Z"
                      fill="#A55BF0" />
                </g>
                <defs>
                  <clipPath id="clip0_27_5293">
                    <rect width="45" height="50" fill="white" />
                  </clipPath>
                </defs>
              </svg>
              </a>
              </li>
            </ul>
          </nav>
          <nav class="footer_content">
            <span class="line line-top">&nbsp;</span>
            <span class="line line-fond">&nbsp;</span>
            <ul class="footer_info">
              <li>
                <h3>Contactenos</h3>
              </li>
              <li class="footer_content-info">
                <img src="../assets/icon_phone.svg" alt="" width="25" height="25">
                <p>+(57) 3225318966</p>
              </li>
              <li class="footer_content-info">
                <img src="../assets/icon_email.svg" alt="" width="25" height="25">
                <p>info@petfect.com</p>
              </li>
              <li class="footer_content-info">
                <img src="../assets/icon_localizacion.svg" alt="" width="25" height="25">
                <p>Transversal 96B #21A - 70 - Bogotá</p>
              </li>
            </ul>
            <ul class="footer_content-list">
              <li>
                <h3>Información</h3>
              </li>
              <li><a href="#about">Sobre Nosotros</a></li>
              <li><a href="#services">Servicios</a></li>
              <li><a href="#experiences">Experiencias</a></li>
            </ul>
            <ul class="footer_content-list">
              <li>
                <h3>Links</h3>
              </li>
              <li><a href="#about">Sobre Nosotros</a></li>
              <li><a href="#services">Servicios</a></li>
              <li><a href="#experiences">Experiencias</a></li>
            </ul>
          </nav>
          <div class="footer_me">
            <p>&copy; 2024 <span class="footer_purple">Petfect</span>. Todos los derechos reservados.</p>
            <p>Desarrollado con ❤️ por <span class="footer_purple">David Casallas</span></p>
          </div>
        </div>
      </div>
    </footer>
  </div>
</template>


<script lang="js" src="../scripts/js/landing/index.js">
</script>

<style scoped>
@import "../styles/css/landing/styles.css";
</style>