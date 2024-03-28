/**
 * @fileoverview Card displays accessability issues + suggestions on the frontend
 */


import { Problem } from "../interfaces/objects";
import { showImage } from "../utils/chrome";

const Card = (props: Problem) => {
    return (
        <div className="flex flex-row  mb-5">

            <img
                src={props.imageUrl}
                alt=""
                width={90}
                height={90}
                style={
                    {
                        objectFit: "contain"
                    }
                }                                               
            >
            </img>

            <div className="flex flex-col prose-sm">
                <div className="flex flex-row justify-between">
                    <p className="font-bold">Type: </p>
                    <p>{props.type}</p>
                </div>
                <div className="flex flex-row justify-between">
                    <p className="font-bold">Suggestion: </p>
                    <p> {props.suggestion}</p>
                </div>

            </div>

        </div>
    );
}

export default Card;