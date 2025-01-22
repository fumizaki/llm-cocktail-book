import {
	Dialog,
	DialogContent,
	DialogDescription,
	DialogHeader,
	DialogTitle,
	DialogTrigger,
} from "@/components/ui/dialog";
import { Button } from "@/components/ui/button";
import { Pencil } from "lucide-react";
import { Chatbot } from "@/domain/schema";

type Props = {
	value: Chatbot;
};

export const EditChatbotDialog = ({ value }: Props) => {
	return (
		<Dialog>
			<DialogTrigger asChild>
				<Button size={"icon"} variant={"ghost"}>
					<Pencil />
				</Button>
			</DialogTrigger>
			<DialogContent>
				<DialogHeader>
					<DialogTitle>Edit Chatbot?</DialogTitle>
					<DialogDescription>Edit {value.title}</DialogDescription>
				</DialogHeader>
			</DialogContent>
		</Dialog>
	);
};
