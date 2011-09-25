<!DOCTYPE html>
<html lang="en">	
	
	<head>		
		
		<meta charset="utf-8">
		<title>[ADD THE PAGE TITLE HERE]</title>
		
		<link rel="stylesheet" href="styles/style.css" />
		
		<script src="https://ajax.googleapis.com/ajax/libs/jquery/1.6.3/jquery.min.js"></script>
		<script src="js/contact-form-process.js"></script>
				
		<!--[if IE 6]>
            <link rel="stylesheet" href="styles/ie6.css" />
        <![endif]--> 
        <!--[if IE 7]>
            <link rel="stylesheet" href="styles/ie7.css" />
        <![endif]--> 
        <!--[if IE 8]>
            <link rel="stylesheet" href="styles/ie8.css" />
        <![endif]-->  
        		
	</head>
	
	<body>	
		
		<div id="wrap">	
			
			<div id="sidebar">
			
				<h1>[ADD YOUR NAME]</h1>
				<h2>[ADD YOUR JOB TITLE]</h2>
				
				<!-- THIS IS THE NAVIGATION AREA - ADD YOUR SITE'S PAGES HERE -->
				<ul id="nav">	
						
					<li><a href="index.php" title="Link To The Home Page">Home</a><span>/</span></li>					
					<li><a href="services.php" title="Link To The Services Page">Services</a><span>/</span></li>
					<li><a href="articles.php" title="Link To The Articles Page">Articles</a><span>/</span></li>
					<li class="current"><a href="contact.php" title="Link To The Contact Page">Contact</a></li>
								
				</ul><!--end nav-->
				
				<div id="bio">
					
					<!-- ADD A PHOTO OF YOURSELF HERE - YOU CAN USE ANY SIZE YOU LIKE, ALTHOUGH THE RECOMMENDED DIMENSIONS ARE 140x150px -->
					<img class="author-img" src="[ADD A URL TO YOUR PHOTO]" alt="Photo of [ADD YOUR NAME]" />	
					
					<h3>About Me</h3>					
					<p>[ADD AN OVERVIEW ABOUT YOURSELF HERE]</p>			
						
				</div><!--end bio-->
				
				<div class="sidebar-line"></div>
				
				<div id="freelance-services">			
					
					<h3>Freelance Services</h3>
					
					<p>[PROVIDE AN OVERVIEW ABOUT YOUR SERVICES HERE]</p>	
					
					<p id="status"><span>Current Status</span>: Taking On New Clients</p>
					
				</div><!--end freelance-services-->
				
				<div class="sidebar-line"></div>			
				
				<div id="testimonials">
				
					<h3>Client Testimonial</h3>
					
					<div class="testimonial">
						
						<p>[ADD A TESTIMONIAL HERE]</p>
						
						<p class="author-details">[ADD TESTIMONIAL AUTHOR NAME]</p>
					
					</div><!--end testimonial-->
					
					<p><a href="#" title="Link To Testimonials Page">View All Testimonials &raquo;</a></p>
	
				</div><!--end testimonials-->
				
				<div id="footer">		
					
					<p>Copyright &copy; 2011 / [ADD YOUR NAME HERE] / All Rights Reserved</p>	
						
				</div><!--end footer-->	
			
			</div><!--end sidebar-->
					
			<div id="content">	

				<p>Please use the form below if you'd like to get in touch with me about any projects that you have in mind. I always aim to respond within 24 hours.</p>
				
				<p class="hide" id="response"></p> 
				
				<!-- BELOW IS THE CODE FOR THE CONTACT FORM - TO GET THIS WORKING YOU'LL NEED TO EDIT LINE 33 IN THE "SCRIPTS/CONTACT-PROCESS.PHP" FILE BY REPLACING THE EMAIL ADDRESS ("your@email.com") WITH YOUR OWN. SAVE YOUR CHANGES AND THE FORM WILL THEN BE FULLY CONFIGURED. -->
					
				<form id="contact-form" method="post" action="scripts/contact-process.php">
								
					<input id="form_name" type="text" name="name" value="Name" onfocus="if(this.value=='Name'){this.value=''};" onblur="if(this.value==''){this.value='Name'};" />					
					<input id="form_email" type="text" name="email" value="Email" onfocus="if(this.value=='Email'){this.value=''};" onblur="if(this.value==''){this.value='Email'};" />
					<input id="form_subject" type="text" name="subject" value="Subject" onfocus="if(this.value=='Subject'){this.value=''};" onblur="if(this.value==''){this.value='Subject'};" />			
					<textarea id="form_message" rows="10" cols="40" name="message"></textarea>				
					<input id="form_submit" class="submit" type="submit" name="submit" value="" />			
					<div class="hide">
						<label>Do not fill out this field</label>
						<input name="spam_check" type="text" value="" />
					</div>
				
				</form><!--end contact-form-->	
						
			</div><!--end content-->
				
		</div><!--end wrap-->	
		
		<div class="cache-images">
			<img src="images/submit-button-orange-hover.jpg" width="0" height="0" alt="" />
		</div><!--end cache-images--> 
				
	</body>
		
</html>