import { useState } from "react";
import { getUrl } from "../utils/chrome";
import { ChangeIsReady } from "../interfaces/functions";
import {checker} from "../utils/checker"

function Stats() {
    return (
        <div className="flex flex-row justify-between">

            <div className="">
                <div>Score</div>
                <div className="flex justify-center items-center bg-primary rounded-full w-12 h-12  ">
                    <p className="font-bold">8.5</p>
                </div>
            </div>
            <div>
                <div className="mb-1"> Score list</div>

                <p className="font-bold">Readability - 8.5</p>
                <p className="font-bold">Alt Text - 8.5</p>



            </div>

        </div>

    )
}

const Header = ({changeIsReady}:{changeIsReady:ChangeIsReady}) => {
    const [init , setInit] = useState<boolean>(false)
    const [website , setWebsite] = useState<string|null>(null)

  
    return (
        <div className="flex flex-col">
            <h1 className="mb-3 text-xl font-bold">Accessability Checker</h1>
            
            <div className="flex flex-row mb-1 w-1/2 ">
              <p>Checking</p>
               <p className="font-bold text-ellipsis ">{ website }</p>
            </div>
           
            {!init ? ( <button
                className="btn btn-secondary mt-5"
                onClick={
                    async ()=>{
                        const url = await getUrl();
                        
                        if(url){
                            checker(url)
                            setWebsite(url); 
                            changeIsReady(true,url as string);
                            setInit(true); 
                        }
                        
                    }
                }
            >
                Analyze website
            </button>): (<Stats />)}

        </div>
    )
}

export default Header;