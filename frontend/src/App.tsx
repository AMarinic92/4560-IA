import Header from "./components/header"
import Problems from "./components/problems"
import Suggestions from "./components/suggestions"


function App() {
  
  return (
   <div className="container h-96 w-full  px-5 py-5">
    <Header />
    <div className="flex flex-col mt-5 ">
      <Problems />
      <Suggestions />
    

    </div>

   </div>
  )
}

export default App
