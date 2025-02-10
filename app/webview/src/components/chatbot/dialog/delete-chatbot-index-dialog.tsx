import {
	Dialog,
	DialogContent,
	DialogDescription,
	DialogHeader,
	DialogTitle,
	DialogTrigger,
} from "@/components/ui/dialog";
import { Button } from "@/components/ui/button";
import { Trash2 } from "lucide-react";
import { ChatbotIndex } from "@/domain/schema";

type Props = {
	value: ChatbotIndex;
};

export const DeleteChatbotIndexDialog = ({ value }: Props) => {
	return (
		<Dialog>
			<DialogTrigger asChild>
				<Button size={"icon"} variant={"ghost"}>
					<Trash2 />
				</Button>
			</DialogTrigger>
			<DialogContent>
				<DialogHeader>
					<DialogTitle>Delete Chatbot Index?</DialogTitle>
					<DialogDescription>Delete {value.title}</DialogDescription>
				</DialogHeader>
			</DialogContent>
		</Dialog>
	);
};
