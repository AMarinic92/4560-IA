/**
 * @fileoverview Card displays accessability issues + suggestions on the frontend
 */


import { Problem } from "../interfaces/objects";
import { showImage } from "../utils/chrome";

const Card = (props:Problem) => {
    return ( 
        <div className="flex flex-row justify-center  mb-5"
        onClick={
            ()=> showImage(props.imageUrl)
        }
        
        >
            <img
                src={props.imageUrl}
                alt=""
                width={90}
                height={90}
                style={
                    {
                        objectFit:"contain"
                    }
                }
            >
            </img>
            <div className="flex flex-col prose">
                    <div className="flex flex-row">
                         <b>Type: </b> 
                         <p>{props.type}</p>
                    </div>
                    <p className="flex flex-row"> 
                        <b>Suggestion:</b>
                        <p>{props.suggestion}</p>
                     </p>
            </div>

        </div>
     );
}
 
export default Card;