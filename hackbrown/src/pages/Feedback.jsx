// import React from "react";
// import Navbar from "../components/Navbar";
// import logoImage from "../assets/brownlogo.png";
// import emailjs from "emailjs-com";

// const Feedback = () => {
//   emailjs.init("ohywxfySYEwoUO--2");
//   const containerStyle = {
//     fontFamily: "'Inter', sans-serif", // Apply Inter font to the entire component
//     backgroundImage: "url('src/assets/homepage-background.png')",
//     backgroundSize: "100% 100%",
//     backgroundRepeat: "no-repeat",
//     height: "100vh", // Set the height to cover the entire viewport height"
//     display: "flex",
//     flexDirection: "column", // If you want to stack Navbar and content vertically
//   };

//   const handleSubmit = async (event) => {
//     event.preventDefault();

//     // Your EmailJS service ID
//     const serviceId = "service_3kjzo0l";

//     // Your EmailJS template ID
//     const templateId = "template_pqnrhll";

//     try {
//       const response = await emailjs.sendForm(
//         serviceId,
//         templateId,
//         event.target // Pass the form data using event.target
//       );

//       // Log success or handle response as needed
//       console.log("Email sent successfully:", response);

//       // Clear form fields after submission
//       event.target.reset();
//     } catch (error) {
//       console.error("Error sending email:", error);
//     }
//   };

//   return (
//     <div style={containerStyle} className="flex flex-col h-lvh">
//       <Navbar />
//       <div className="flex flex-row">
//         <div className="w-1/2"></div>
//         <div className="mx-20 flex flex-col flex-grow w-1/2 p-2 h-lvh space-y-8">
//           <h2 className="mb-4 text-4xl tracking-tight font-extrabold text-center text-white">
//             Contact Us
//           </h2>
//           <p className="mb-8 lg:mb-16 font-light text-center text-gray-400 sm:text-xl"></p>
//           <form onSubmit={handleSubmit} className="space-y-8">
//             <div>
//               <label
//                 for="hackatbrown1@gmail.com"
//                 class="block mb-2 text-sm font-medium text-gray-300"
//               >
//                 Your email
//               </label>
//               <input
//                 type="email"
//                 id="message"
//                 class="shadow-sm p-3 w-full bg-white border-gray-600 placeholder-gray-400 text-gray-600 focus:ring-primary-500 focus: border-primary-500 shadow-sm-light rounded-lg"
//                 placeholder="name@flowbite.com"
//                 required
//               />
//             </div>
//             <div>
//               <label
//                 for="subject"
//                 class="block mb-2 text-sm font-medium text-gray-300 ri"
//               >
//                 Subject
//               </label>
//               <input
//                 type="text"
//                 id="subject"
//                 class="block p-3 w-full text-sm bg-white border-gray-600 placeholder-gray-400 text-gray-600 focus:ring-primary-500 focus:border-primary-500 shadow-sm-light rounded-lg"
//                 placeholder="Let us know how we can help you"
//                 required
//               ></input>
//             </div>
//             <div>
//               <label
//                 for="message"
//                 class="block mb-2 text-sm font-medium text-white"
//               >
//                 Your message
//               </label>
//               <textarea
//                 id="message"
//                 rows="6"
//                 class="block p-2.5 w-full text-sm bg-white text-gray-600 bg-primary-600 placeholder-gray-400 focus:ring-primay-500 focus:border-primary-500 rounded-lg"
//                 placeholder="Leave a comment..."
//               ></textarea>
//             </div>
//             <button
//               type="submit"
//               class="py-3 px-5 text-sm font-medium text-center text-white bg-blue-700 bg-primary-600 hover:bg-primary-700 focus:ring-primary-800 focus:outline-none focus:ring-4 rounded-lg"
//             >
//               Send Message
//             </button>
//           </form>
//         </div>
//       </div>
//     </div>
//   );
// };

// export default Feedback;
