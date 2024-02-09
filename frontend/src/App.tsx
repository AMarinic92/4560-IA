import Header from "./components/header"
import Suggestions from "./components/suggestions"


function App() {
  
  return (
   <div className="container h-96 w-80  px-5 py-10">
    <Header />
    <div className="flex flex-col mt-5 ">
      <Suggestions />
    

    </div>

   </div>
  )
}

export default App
