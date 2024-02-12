import { useState } from "react"
import Header from "./components/header"
import Problems from "./components/problems"
import Suggestions from "./components/suggestions"


function App() {

  const [isReady, setIsReady] = useState<boolean>(false)

  return (
    <div className="container h-96 w-full  px-5 py-5">
      <Header
        changeIsReady={
          (val: boolean) => {
            setIsReady(val)
          }
        }
      />

      {
        isReady ? (<div className="flex flex-col mt-5 ">

          <Problems />
          <Suggestions />



        </div>
        ) : ""
      }


    </div>
  )
}

export default App
