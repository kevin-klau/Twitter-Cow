import Link from "next/link"; 
import Dropdown from 'react-dropdown'
import 'react-dropdown/style.css';
import { BsFillMoonStarsFill } from "react-icons/bs";


export default function NavBar(){
    return(
        <nav className="py-10 mb-12 flex justify-between">
              <li>
                    <Link href={"/"}>
                        <li className="text-teal-700">Home</li>
                    </Link>
                    <Link href={"/contact"}>
                        <li className="text-teal-700">More</li>
                    </Link>
                    <li>BsFillMoonStarsFil </li>
              </li>
        </nav>
    );
}