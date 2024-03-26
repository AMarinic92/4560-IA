import { useState } from "react";
import { getUrl } from "../utils/chrome";
import { ChangeIsReady } from "../interfaces/functions";
import {checker} from "../utils/checker"


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
            </button>): ("")}

        </div>
    )
}

export default Header;